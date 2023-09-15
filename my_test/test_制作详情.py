from PIL import Image
from tqdm import tqdm

from fun_制作详情.fun_8_裁剪图片 import fun_裁剪图片
from fun_制作详情.run_制作详情 import run_制作文件夹详情
from fun_制作详情.type import MakeXQModel

root_path = r"F:\小夕素材\10000-10999"
material_id = "10064"

im = run_制作文件夹详情(
    MakeXQModel(
        image_dir_path=rf"{root_path}\{material_id}\预览图",
        use_image=13,
        sort=True,
        line_num=2,
        line_ratio=1.5,
        material_path=rf"{root_path}\{material_id}\{material_id}",
        has_info=True,
        xq_width=1500,
        spacing=30,
        crop_position="start",
    )
)

for x, im in tqdm(
    list(enumerate(fun_裁剪图片(im=im, oneline_height=2500))),
    ncols=100,
    desc="裁剪详情图片\t",
):
    x: int
    im: Image.Image
    im.save(rf"C:\Users\wuweihua\Desktop\UPLOAD\{x+1}.png")
