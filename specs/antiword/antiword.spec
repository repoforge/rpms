# $Id$
# Authority: dries
# Upstream: Andri van Os <antiword$winfield,demon,nl>

Summary: Converts MS-Word documents to ASCII and Postscript
Name: antiword
Version: 0.36.1
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://www.winfield.demon.nl/

Source: http://www.winfield.demon.nl/linux/antiword-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 

%description
Antiword is a free MS-Word reader. It converts the documents from Word 2, 
6, 7, 97, 2000, 2002, and 2003 to text, Postscript, and XML/DocBook. 
Antiword tries to keep the layout of the document intact.

%prep
%setup

%build
%{__make} %{?_smp_mflags} LOCAL_INSTALL_DIR=%{_bindir} LOCAL_RESOURCES_DIR=%{_datadir}/antiword

%install
%{__rm} -rf %{buildroot}
%makeinstall LOCAL_INSTALL_DIR=%{buildroot}%{_bindir} LOCAL_RESOURCES_DIR=%{buildroot}%{_datadir}/antiword

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Docs/*
%{_bindir}/antiword
%{_bindir}/kantiword
%{_datadir}/antiword/

%changelog
* Thu Sep 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.36.1
- Initial package.
