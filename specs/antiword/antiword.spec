# $Id$
# Authority: dries
# Upstream: Andri van Os <antiword$winfield,demon,nl>

Summary: Converts MS-Word documents to ASCII and Postscript
Name: antiword
Version: 0.37
Release: 3
License: GPL
Group: Applications/File
URL: http://www.winfield.demon.nl/

Source: http://www.winfield.demon.nl/linux/antiword-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Antiword is a free MS-Word reader. It converts the documents from
Word 2, 6, 7, 97, 2000, 2002, and 2003 to text, Postscript, and
XML/DocBook. Antiword tries to keep the layout of the document
intact.

%prep
%setup

%build
%{__make} %{?_smp_mflags} LOCAL_INSTALL_DIR="%{_bindir}" LOCAL_RESOURCES_DIR="%{_datadir}/antiword"

%install
%{__rm} -rf %{buildroot}
%makeinstall LOCAL_INSTALL_DIR="%{buildroot}%{_bindir}" LOCAL_RESOURCES_DIR="%{buildroot}%{_datadir}/antiword"

%{__install} -Dp -m0644 Docs/antiword.1 %{buildroot}%{_mandir}/man1/antiword.1

%{__chmod} a+rx %{buildroot}%{_bindir}/antiword
%{__chmod} a+rx %{buildroot}%{_bindir}/kantiword

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Docs/*
%doc %{_mandir}/man1/antiword.1*
%{_bindir}/antiword
%{_bindir}/kantiword
%{_datadir}/antiword/

%changelog
* Mon Mar 17 2008 Dag Wieers <dag@wieers.com> - 0.37-3
- Installed manpage.

* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 0.37-2
- Change permissions of antiword, thanks to Tim Wegener and Michael Mansour.

* Tue Nov 29 2005 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Updated to release 0.37.

* Thu Sep 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.36.1
- Initial package.
