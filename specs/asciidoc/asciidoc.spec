# $id$
# Authority: dag

Summary: Tool to convert AsciiDoc text files to DocBook, HTML or LinuxDoc
Name: asciidoc
Version: 7.0.1
Release: 1
License: GPL
Group: Applications/Text
URL: http://www.methods.co.nz/asciidoc/

Source: http://www.methods.co.nz/asciidoc/%name-%version.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
Requires: python

%description
AsciiDoc is a text document format for writing short documents, articles,
books and UNIX man pages.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/asciidoc/
%{__install} -p -m0644 *.conf %{buildroot}%{_sysconfdir}/asciidoc/

%{__install} -Dp -m0644 filters/code-filter.conf %{buildroot}%{_sysconfdir}/asciidoc/filters/code-filter.conf
%{__install} -Dp -m0755 filters/code-filter.py %{buildroot}%{_sysconfdir}/asciidoc/filters/code-filter.py

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/asciidoc/stylesheets/
%{__install} -p -m0644 stylesheets/*.css %{buildroot}%{_sysconfdir}/asciidoc/stylesheets/

%{__install} -Dp -m0755 asciidoc.py %{buildroot}%{_datadir}/asciidoc/asciidoc.py

%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f %{_datadir}/asciidoc/asciidoc.py %{buildroot}%{_bindir}/asciidoc

%{__install} -d -m0755 %{buildroot}%{_datadir}/asciidoc/
%{__cp} -pR images/ %{buildroot}%{_datadir}/asciidoc/

%{__install} -Dp -m0644 doc/asciidoc.1 %{buildroot}%{_mandir}/man1/asciidoc.1

%clean
%{__rm} -rf %{buildroot}

%files
%doc BUGS BUGS.txt CHANGELOG CHANGELOG.txt COPYRIGHT README README.txt
%doc doc/*.txt examples/ filters/*.txt
%doc %{_mandir}/man1/asciidoc.1.*
%config(noreplace) %{_sysconfdir}/asciidoc/
%{_bindir}/asciidoc
%{_datadir}/asciidoc/
%{_datadir}/asciidoc/

%changelog
* Wed Aug 10 2005 Dag Wieers <dag@wieers.com> - 7.0.1-1
- Initial package. (using DAR)
