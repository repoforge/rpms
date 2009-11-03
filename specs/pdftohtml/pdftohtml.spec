# $Id$

# Authority: dries
# Upstream:

Summary: Converts PDF files into HTML and XML formats
Name: pdftohtml
Version: 0.36
Release: 1.2%{?dist}
License: GPL
Group: Applications/Text
URL: http://pdftohtml.sourceforge.net/

Source: http://dl.sf.net/pdftohtml/pdftohtml-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Pdftohtml is a tool based on the Xpdf package which translates pdf documents
into html format.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp pdftohtml %{buildroot}%{_bindir}/pdftohtml

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.36-1.2
- Rebuild for Fedora Core 5.

* Fri Jul 30 2004 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Initial package.
