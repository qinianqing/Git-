import inquirer
from inquirer import errors
import os

def commit_shell():
  def msg_validation(answers, current):
        if current == '':
          raise errors.ValidationError('', reason='请输入要提交的内容!')
        return True

  questions = [
      inquirer.List('type',
                    message="请选择本次提交的类型:",
                    choices=[
                    '✨  引入新特性',
                    '🎨  优化代码的结构/格式',
                    '🐛  修复 bug',
                    '⚡️  提升性能',
                    '🔥  删除代码或文件',
                    '💄  更新界面和样式文件',
                    '🔧  更改配置文件',
                    '🚧  工作进行中',
                    '🚑 重要补丁',
                    '📝  撰写文档',
                    '✅  增加测试',
                    '📦  更新打包文件',
                    '🎉  初次提交',
                    '🔖  发布/版本标签',
                    '🚀  部署功能',
                    '💚 修复CI构建问题',
                    '👷  CI编译系统',
                    '🌐  国际化与本地化'
                    ]
                  ),
      inquirer.Text('msg',message="请输入要提交的文本",validate=msg_validation,),
      inquirer.List('branch',
                    message="请选择本次提交的分支:",
                    choices=[
                      'dev',
                      'test'
                    ]
                   )         
  ]

  answers = inquirer.prompt(questions)
  return answers

if __name__ == "__main__":
  os.system('git add .')  
  os.system('git status')
  result = commit_shell()
  commit_msg = "git commit -m '{type} {msg}'".format(type=result['type'],msg=result['msg'])
  os.system(commit_msg)
  commit_push = "git push origin {}".format(result['branch'])
  os.system(commit_push)

