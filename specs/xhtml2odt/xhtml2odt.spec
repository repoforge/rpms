# $Id$
# Authority: dag

Summary: Tool to convert from XHTML to ODT
Name: xhtml2odt
Version: 1.2
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://xhtml2odt.org/

Source: http://xhtml2odt.org/dl/xhtml2odt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: help2man
BuildRequires: python
BuildRequires: python-imaging
BuildRequires: python-lxml
BuildRequires: python-tidy
BuildRequires: rpm-macros-rpmforge
Requires: python
Requires: python-imaging
Requires: python-lxml
Requires: python-tidy

%filter_provides_in %{_docdir} 
%filter_requires_in %{_docdir}
%filter_setup

%description
XHTML2ODT is a converting library from XHTML to ODT. It is based on XSL
stylesheets for portability, and is designed to help web applications
export to the ODT document format. 

%prep
%setup

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc template.odt xhtml2odt.php xhtml2odt.sh *.txt
%doc %{_mandir}/man1/xhtml2odt.1*
%{_bindir}/xhtml2odt
%{_datadir}/xhtml2odt/

%changelog
* Thu Sep 23 2010 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
