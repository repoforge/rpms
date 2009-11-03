# $id$
# Authority: dag

Summary: Tool to convert AsciiDoc text files to DocBook, HTML or Unix man pages
Name: asciidoc
Version: 5.1.1
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://www.methods.co.nz/asciidoc/

Source: http://dl.sf.net/asciidoc/asciidoc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.1
Requires: python >= 2.1

%description
AsciiDoc is a text document format for writing short documents, articles,
books and UNIX man pages.

%prep
%setup

### FIXME: Hardcode /etc/asciidoc for systemwide installation
%{__perl} -pi.orig -e 's|APP_DIR = .+$|APP_DIR = "/etc/asciidoc"|g' asciidoc.py

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/asciidoc/{filters,stylesheets}
%{__install} -p -m0644 *.conf %{buildroot}%{_sysconfdir}/asciidoc/
%{__install} -p -m0644 filters/code-filter.{conf,py} %{buildroot}%{_sysconfdir}/asciidoc/filters/
%{__install} -p -m0644 stylesheets/*.css %{buildroot}%{_sysconfdir}/asciidoc/stylesheets/
%{__cp} -pR images/ %{buildroot}%{_sysconfdir}/asciidoc/

%{__install} -Dp -m0755 asciidoc.py %{buildroot}%{_bindir}/asciidoc
%{__install} -Dp -m0644 doc/asciidoc.1 %{buildroot}%{_mandir}/man1/asciidoc.1

%{__install} -d -m0755 %{buildroot}%{_datadir}/asciidoc/
%{__cp} -pR images/ stylesheets/ %{buildroot}%{_datadir}/asciidoc/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG* COPYING COPYRIGHT README*
%doc doc/*.txt examples/ filters/*.txt
%doc %{_mandir}/man1/asciidoc.1*
%config(noreplace) %{_sysconfdir}/asciidoc/
%{_bindir}/asciidoc
%{_datadir}/asciidoc/

%changelog
* Wed Jun 14 2006 Dag Wieers <dag@wieers.com> - 5.1.1-1
- Initial package. (using DAR)
