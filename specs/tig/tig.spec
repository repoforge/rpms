# $Id$
# Authority: shuff
# Upstream: Jonas Fonseca <fonseca$diku,dk>

Summary: Text-mode interface for git
Name: tig
Version: 0.18
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://jonas.nitro.dk/tig/

Source: http://jonas.nitro.dk/tig/releases/tig-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: asciidoc >= 8.4
BuildRequires: docbook-style-xsl
BuildRequires: docbook-utils
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: ncurses-devel
BuildRequires: rpm-macros-rpmforge
BuildRequires: xmlto
BuildRequires: /usr/bin/iconv
Requires: bash-completion
Requires: git-core

%description
Tig allows you to browse changes in a git repository and can additionally act
as a pager for output of various git commands. When used as a pager, it will
display input from stdin and colorize it.

When browsing repositories, tig uses the underlying git commands to present the
user with various views, such as summarized commit log and showing the commit
with the log message, diffstat, and the diff.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install install-doc DESTDIR="%{buildroot}"

# bash completion
%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/bash_completion.d/
%{__install} -m0755 contrib/tig-completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/tig

# stupid install-doc
%{__install} -m0755 -d tigdocs
%{__mv} %{buildroot}%{_docdir}/tig/* tigdocs/
%{__rm} -rf %{buildroot}%{_docdir}/tig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS COPYING INSTALL NEWS* README* SITES TODO VERSION contrib/ tigdocs/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_sysconfdir}/bash_completion.d/tig

%changelog
* Tue Aug 30 2011 Steve Huff <shuff@vecna.org> - 0.18-1
- Updated to version 0.18.

* Thu Apr 21 2011 Steve Huff <shuff@vecna.org> - 0.17-1
- Updated to version 0.17.

* Thu Dec 23 2010 Steve Huff <shuff@vecna.org> - 0.16.2-2
- Gah, wrong path for bash-completion support :(

* Mon Nov 08 2010 Steve Huff <shuff@vecna.org> - 0.16.2-1
- Initial package.
