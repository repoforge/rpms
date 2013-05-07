# $Id$
# Authority: shuff
# Upstream: TaskWarrior <support$taskwarrior,org>

Summary: Command-line todo task manager
Name: task
Version: 2.2.0
Release: 1%{?dist}
License: GPL
Group: Applications/Utilities
URL: http://taskwarrior.org/

Source: http://www.taskwarrior.org/download/task-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cmake >= 2.8
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: lua-devel >= 5.1
BuildRequires: ncurses-devel
Requires: vramsteg

%description
Taskwarrior is a command-line todo list manager.  It maintains a list of tasks
that you want to do, allowing you to add/remove, and otherwise manipulate them.
Task has a rich list of subcommands that allow you to do sophisticated things
with it. You'll find it has customizable reports, charts, GTD features, Lua
extensions, device synching and more.

%package -n vim-task
Summary: Vim support for TaskWarrior
Group: Applications/Text
Requires: %{name} = %{version}-%{release}
Requires: vim-common

%description -n vim-%{name}
This package provides Vim support for TaskWarrior.

%package -n fish-task
Summary: Fish support for TaskWarrior
Group: Applications/Shells
Requires: %{name} = %{version}-%{release}
Requires: fish

%description -n fish-%{name}
This package provides Fish completion support for TaskWarrior.

%package -n bash-task
Summary: Bash support for TaskWarrior
Group: Applications/Shells
Requires: %{name} = %{version}-%{release}
Requires: bash-completion

%description -n bash-%{name}
This package provides Bash completion support for TaskWarrior.

%prep
%setup

%build
%ifarch x86_64
%define cmake_flags -DCMAKE_INSTALL_PREFIX=%{_prefix}
%else
%define cmake_flags -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_C_FLAGS=-m32 -DCMAKE_CXX_FLAGS=-m32 -DCMAKE_EXE_LINKER_FLAGS=-m32
%endif

%{cmake} %{cmake_flags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix the docdir
%{__mv} %{buildroot}%{_docdir}/task %{buildroot}%{_docdir}/task-%{version}

# install Vim support files
%{__install} -m755 -d %{buildroot}%{_datadir}/vim/vim70/ftdetect
%{__install} -m755 -d %{buildroot}%{_datadir}/vim/vim70/syntax
%{__install} -m644 scripts/vim/ftdetect/*.vim %{buildroot}%{_datadir}/vim/vim70/ftdetect
%{__install} -m644 scripts/vim/syntax/*.vim %{buildroot}%{_datadir}/vim/vim70/syntax

# install Fish support files
%{__install} -m755 -d %{buildroot}%{_datadir}/fish/completions
%{__install} -m644 scripts/fish/task.fish %{buildroot}%{_datadir}/fish/completions

# install Bash support files
%{__install} -m755 -d %{buildroot}%{_sysconfdir}/bash_completion.d
%{__install} -m644 scripts/bash/task.sh %{buildroot}%{_sysconfdir}/bash_completion.d/task

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_docdir}/task-%{version}/*
%{_bindir}/*

%files -n vim-task
%defattr(-, root, root, 0644)
%{_datadir}/vim/vim70/*/*.vim

%files -n fish-task
%defattr(-, root, root, 0644)
%{_datadir}/fish/completions/task.fish

%files -n bash-task
%defattr(-, root, root, 0644)
%{_sysconfdir}/bash_completion.d/task

%changelog
* Tue May 07 2013 David Hrbáč <david@hrbac.cz> - 2.2.0
- new upstream release

* Fri Aug  3 2012 Steve Huff <shuff@vecna.org> - 2.1.1-1
- Initial package.
