
import uuid
import lxml.etree as etree


def extract_slide_mapping(slidelist):
    """this method will get the mapping between a slide_id and rID. This is necessary to maintain the xml syntax valid
    after injection / modification"""

    slide_mapping = dict()

    for slide in slidelist:
        rid = slide.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
        slide_id = slide.attrib['id']
        slide_mapping[slide_id] = rid

    return slide_mapping


def prepare_sections(keys, presentation, mapping, all_sections=False):
    """this method will prepare a xml tree based on the passed section names the user wants to have in 
    the pptx"""

    nmap = presentation.slides._sldIdLst.nsmap

    all_sections = compile_sections(presentation, mapping)
    root = etree.Element(
        '{http://schemas.openxmlformats.org/presentationml/2006/main}sldIdLst', nsmap=nmap)

   
    if (all_sections) and (len(keys) != 0):
        for key in keys:
            section = all_sections[key]

            for slide in section:
                etree.SubElement(
                    root, '{http://schemas.openxmlformats.org/presentationml/2006/main}sldId', attrib=slide, nsmap=nmap)

    return root


def compile_sections(presentation, mapping):
    """this method will get all the sections that are in the pptx"""

    ns = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
    xml = etree.fromstring(presentation.part.blob)
    nsmap = {'p14': 'http://schemas.microsoft.com/office/powerpoint/2010/main'}
    sections = xml.xpath('.//p14:sectionLst', namespaces=nsmap)[0]

    collector = dict()
    pairs_col = list()

    for section in sections:
        key = section.attrib['name']

        for slidelist in section:
            for slide in slidelist:
                pairs = dict()
                slide_id = slide.attrib['id']

                # lookup in slide mapping to get rID
                rID = mapping[slide_id]

                pairs['id'] = slide_id
                pairs[ns] = rID

                pairs_col.append(pairs)

        collector[key] = pairs_col
        pairs_col = list()

    return collector


def replace_slides(new_xml, presentation, folder, save=False):
    """This method will take a xml tree and create the final pptx out of it"""
    uid = str(uuid.uuid4().hex)[:10]
    file_path = f"{folder}/{uid}.pptx"
    slidelist = presentation.slides._sldIdLst

    slidelist.getparent().replace(slidelist, new_xml)

    if save:
        presentation.save(file_path)

    return file_path


def _print_xml(xml):
    print(etree.tostring(xml, pretty_print=True, encoding="unicode"))
