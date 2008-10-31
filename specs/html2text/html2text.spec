# $Id$
# Authority: dag

Summary: Utility to convert HTML document to plain text
Name: html2text
Version: 1.3.2a
Release: 1
License: GPL
Group: Applications/Text
URL: http://www.mbayer.de/html2text/

Source: http://www.mbayer.de/html2text/downloads/html2text-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
html2text is a command line utility, written in C++, that converts HTML
documents into plain text.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
gunzip html2text.1.gz html2textrc.5.gz
%{__install} -Dp -m0755 html2text %{buildroot}%{_bindir}/html2text
%{__install} -Dp -m0644 html2text.1 %{buildroot}%{_mandir}/man1/html2text.1
%{__install} -Dp -m0644 html2textrc.5 %{buildroot}%{_mandir}/man5/html2textrc.5

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING CREDITS INSTALL KNOWN_BUGS RELEASE_NOTES README TODO
%doc %{_mandir}/man1/html2text.1*
%doc %{_mandir}/man5/html2textrc.5*
%{_bindir}/html2text

%changelog
* Wed Oct 29 2008 Dag Wieers <dag@wieers.com> - 1.3.2a-1
- Initial package. (using DAR)
