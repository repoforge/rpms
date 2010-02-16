# $Id$
# Authority: shuff
# Upstream: Aristotle Pagaltzis <pagaltzis$gmx,de>

%define git_tag bdee419
%define real_name ap-perldoc-complete-%{git_tag}

Summary: A bash completion helper for perldoc
Name: bash-completion-perl
Version: 20100215
Release: 1%{?dist}
License: GPL
Group: System Environment/Shells
URL: http://github.com/ap/perldoc-complete

Source: http://download.github.com/ap-perldoc-complete-%{git_tag}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: bash-completion

%description
Install this package to enable tab-completion of functions and installed
modules with the perldoc command.

%prep
%setup -n %{real_name}

%build
%{__cat} <<COMPLETION >perldoc 
# bash completion for perldoc

alias pod=perldoc
complete -C perldoc-complete perldoc
complete -C perldoc-complete pod
COMPLETION

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}/
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/bash_completion.d/
%{__install} -Dp -m0755 perldoc-complete %{buildroot}%{_bindir}
%{__install} -Dp -m0755 perldoc %{buildroot}%{_sysconfdir}/bash_completion.d/

%clean
%{__rm} -rf %{buildroot}

%post
/etc/profile.d/bash_completion.sh

%postun
/etc/profile.d/bash_completion.sh

%files
%defattr(-, root, root, 0755)
%doc README.mkd
%config %{_sysconfdir}/bash_completion.d/*
%{_bindir}/*

%changelog
* Tue Feb 16 2010 Steve Huff <shuff@vecna.org> - 20100215-1
- Initial package.
