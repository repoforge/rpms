# $id$
# Authority: dag

Summary: Tool to convert AsciiDoc text files to DocBook, HTML or Unix man pages
Name: asciidoc
Version: 8.1.0
Release: 1
License: GPL
Group: Applications/Text
URL: http://www.methods.co.nz/asciidoc/

Source: http://dl.sf.net/asciidoc/asciidoc-%{version}.tar.gz
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
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/asciidoc/{docbook-xsl,filters,images/icons,javascripts,stylesheets}/
%{__install} -p -m0644 *.conf %{buildroot}%{_sysconfdir}/asciidoc/
%{__install} -p -m0644 docbook-xsl/*.xsl %{buildroot}%{_sysconfdir}/asciidoc/docbook-xsl/
%{__install} -p -m0644 filters/*.conf %{buildroot}%{_sysconfdir}/asciidoc/filters/
%{__install} -p -m0755 filters/*.py %{buildroot}%{_sysconfdir}/asciidoc/filters/
%{__install} -p -m0644 javascripts/*.js %{buildroot}%{_sysconfdir}/asciidoc/javascripts/
%{__install} -p -m0644 stylesheets/*.css %{buildroot}%{_sysconfdir}/asciidoc/stylesheets/
%{__cp} -pR images/ %{buildroot}%{_sysconfdir}/asciidoc/

%{__install} -Dp -m0755 asciidoc.py %{buildroot}%{_bindir}/asciidoc
%{__install} -Dp -m0755 a2x %{buildroot}%{_bindir}/a2x
%{__install} -Dp -m0644 doc/asciidoc.1 %{buildroot}%{_mandir}/man1/asciidoc.1
%{__install} -Dp -m0644 doc/a2x.1 %{buildroot}%{_mandir}/man1/a2x.1

%{__install} -d -m0755 %{buildroot}%{_datadir}/asciidoc/
%{__cp} -pR images/ stylesheets/ %{buildroot}%{_datadir}/asciidoc/

### Fix symlinks in examples/
%{__install} -d -m0755 symlinks/
%{__ln_s} -f %{_sysconfdir}/asciidoc/filters/ symlinks/filters
%{__ln_s} -f %{_sysconfdir}/asciidoc/images/ symlinks/images
%{__ln_s} -f %{_sysconfdir}/asciidoc/javascripts/ symlinks/javascripts
%{__ln_s} -f %{_sysconfdir}/asciidoc/stylesheets/ symlinks/stylesheets

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS* CHANGELOG* COPYING COPYRIGHT INSTALL* README*
%doc doc/ examples/ symlinks/*
%doc %{_mandir}/man1/a2x.1*
%doc %{_mandir}/man1/asciidoc.1*
%config(noreplace) %{_sysconfdir}/asciidoc/
%{_bindir}/a2x
%{_bindir}/asciidoc
%{_datadir}/asciidoc/

%changelog
* Sat Nov 11 2006 Dag Wieers <dag@wieers.com> - 8.1.0-1
- Updated to release 8.1.0.

* Thu Oct 19 2006 Dag Wieers <dag@wieers.com> - 8.0.0-1
- Updated to release 8.0.0.

* Wed Jun 14 2006 Dag Wieers <dag@wieers.com> - 7.1.2-2
- Installation fixes.

* Thu Mar 09 2006 Dag Wieers <dag@wieers.com> - 7.1.2-1
- Updated to release 7.1.2.

* Fri Aug 12 2005 Dag Wieers <dag@wieers.com> - 7.0.1-3
- Add missing deffatr(). (Alain Rykaert)
- Put asciidoc in %%{_bindir}, instead of a symlink.

* Wed Aug 10 2005 Dag Wieers <dag@wieers.com> - 7.0.1-1
- Initial package. (using DAR)
