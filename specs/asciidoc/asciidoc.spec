# $id$
# Authority: dag

Summary: Tool to convert AsciiDoc text files to DocBook, HTML or Unix man pages
Name: asciidoc
Version: 7.1.2
Release: 1.2
License: GPL
Group: Applications/Text
URL: http://www.methods.co.nz/asciidoc/

Source: http://www.methods.co.nz/asciidoc/asciidoc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.3
Requires: python >= 2.3

%description
AsciiDoc is a text document format for writing short documents, articles,
books and UNIX man pages.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/asciidoc/stylesheets/
%{__install} -p -m0644 stylesheets/xhtml*.css %{buildroot}%{_sysconfdir}/asciidoc/stylesheets/
%{__install} -p -m0644 *.conf %{buildroot}%{_sysconfdir}/asciidoc/

%{__install} -Dp -m0644 filters/code-filter.conf %{buildroot}%{_sysconfdir}/asciidoc/filters/code-filter.conf
%{__install} -Dp -m0755 filters/code-filter.py %{buildroot}%{_sysconfdir}/asciidoc/filters/code-filter.py

%{__install} -Dp -m0755 asciidoc.py %{buildroot}%{_bindir}/asciidoc
%{__install} -Dp -m0644 doc/asciidoc.1 %{buildroot}%{_mandir}/man1/asciidoc.1

%{__install} -d -m0755 %{buildroot}%{_datadir}/asciidoc/
%{__cp} -pR images/ stylesheets/ %{buildroot}%{_datadir}/asciidoc/


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGELOG COPYRIGHT README
%doc doc/*.txt examples/ filters/*.txt
%doc %{_mandir}/man1/asciidoc.1*
%config(noreplace) %{_sysconfdir}/asciidoc/
%{_bindir}/asciidoc
%{_datadir}/asciidoc/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 7.1.2-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 09 2006 Dag Wieers <dag@wieers.com> - 7.1.2-1
- Updated to release 7.1.2.

* Fri Aug 12 2005 Dag Wieers <dag@wieers.com> - 7.0.1-3
- Add missing deffatr(). (Alain Rykaert)
- Put asciidoc in %%{_bindir}, instead of a symlink.

* Wed Aug 10 2005 Dag Wieers <dag@wieers.com> - 7.0.1-1
- Initial package. (using DAR)
