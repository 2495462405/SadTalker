import click
import text2audio
# TEXT = "你好呀！我是老张！"
if __name__=="__main__":
    try:
        text2audio.run(None, None, 'text2audio/default.wav', False, 'mpv')
    except Exception as ex:
        print(ex)
        raise
        sys.exit(1)