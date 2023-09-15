from pathlib import Path

import pythoncom
from pywintypes import com_error
from win32com.client import DispatchEx


def fun_导出操作(ppt_file: str) -> Path:
    ppt_path_obj = Path(ppt_file)

    app = DispatchEx("PowerPoint.Application")
    app.DisplayAlerts = 0
    ppt = app.Presentations.Open(ppt_file)
    ppt.SaveAs((ppt_path_obj.parent / ppt_path_obj.stem).as_posix(), 17)

    save_path = ppt_path_obj
    if ppt_path_obj.suffix.lower() == ".ppt":
        save_path = ppt_path_obj.with_suffix(".pptx")

    ppt.SaveAs(save_path.as_posix())
    ppt.Close()

    return save_path
