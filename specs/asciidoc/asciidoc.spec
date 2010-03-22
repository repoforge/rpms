# $id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Tool to convert AsciiDoc text files to DocBook, HTML or Unix man pages
Name: asciidoc
Version: 8.5.3
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://www.methods.co.nz/asciidoc/

Source: http://dl.sf.net/asciidoc/asciidoc-%{version}.tar.gz
# http://groups.google.com/group/asciidoc/browse_thread/thread/7f7a633c5b11ddc3
Patch0: asciidoc-8.4.5-datadir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.4
Requires: python >= 2.4

%description
AsciiDoc is a text document format for writing short documents, articles,
books and UNIX man pages. AsciiDoc files can be translated to HTML and
DocBook markups using the asciidoc(1) command.

%prep
%setup
%patch0 -p1 -b .datadir

%build
%configure

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
# real conf data goes to sysconfdir, rest to datadir; symlinks so asciidoc works
for d in dblatex docbook-xsl images javascripts stylesheets ; do
    mv %{buildroot}%{_sysconfdir}/asciidoc/$d \
        %{buildroot}%{_datadir}/asciidoc
    ln -s %{_datadir}/asciidoc/$d %{buildroot}%{_sysconfdir}/asciidoc/
done

# Python API
install -Dpm 644 asciidocapi.py %{buildroot}%{python_sitelib}/asciidocapi.py

# Make it easier to %exclude these with both rpm < and >= 4.7
for file in %{buildroot}{%{_bindir},%{_datadir}/asciidoc/filters/*}/*.py ; do
    touch ${file}{c,o}
done

#%{__install} -Dp -m0755 asciidoc.py %{buildroot}%{_bindir}/asciidoc
#%{__install} -Dp -m0755 a2x %{buildroot}%{_bindir}/a2x
#%{__install} -Dp -m0644 doc/asciidoc.1 %{buildroot}%{_mandir}/man1/asciidoc.1
#%{__install} -Dp -m0644 doc/a2x.1 %{buildroot}%{_mandir}/man1/a2x.1

#%{__install} -d -m0755 %{buildroot}%{_datadir}/asciidoc/
#%{__cp} -pR docbook-xsl/ images/ javascripts/ stylesheets/ %{buildroot}%{_datadir}/asciidoc/

#%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/asciidoc/
#%{__install} -p -m0644 *.conf %{buildroot}%{_sysconfdir}/asciidoc/
#%{__cp} -pR filters/ %{buildroot}%{_sysconfdir}/asciidoc/
#%{__ln_s} -f %{_datadir}/asciidoc/docbook-xsl/ %{buildroot}%{_sysconfdir}/asciidoc/
#%{__ln_s} -f %{_datadir}/asciidoc/images/ %{buildroot}%{_sysconfdir}/asciidoc/
#%{__ln_s} -f %{_datadir}/asciidoc/javascripts/ %{buildroot}%{_sysconfdir}/asciidoc/
#%{__ln_s} -f %{_datadir}/asciidoc/stylesheets/ %{buildroot}%{_sysconfdir}/asciidoc/

### Fix symlinks in examples/
#%{__install} -d -m0755 symlinks/
#%{__ln_s} -f %{_sysconfdir}/asciidoc/filters/ symlinks/filters
#%{__ln_s} -f %{_sysconfdir}/asciidoc/images/ symlinks/images
#%{__ln_s} -f %{_sysconfdir}/asciidoc/javascripts/ symlinks/javascripts
#%{__ln_s} -f %{_sysconfdir}/asciidoc/stylesheets/ symlinks/stylesheets

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS* CHANGELOG* COPYING COPYRIGHT INSTALL* README*
%doc doc/ examples/ vim/
%doc %{_mandir}/man1/a2x.1*
%doc %{_mandir}/man1/asciidoc.1*
%config(noreplace) %{_sysconfdir}/asciidoc/
%{_bindir}/a2x
%{_bindir}/a2x.py
%{_bindir}/asciidoc
%{_bindir}/asciidoc.py
%{_datadir}/asciidoc/
%{python_sitelib}/asciidocapi.py*
%exclude %{_bindir}/*.py[co]
%exclude %{_datadir}/asciidoc/filters/*/*.py[co]

%changelog
* Tue Jan 26 2010 Dag Wieers <dag@wieers.com> - 8.5.3-1
- Updated to release 8.5.3.

* Tue Nov 03 2009 Dag Wieers <dag@wieers.com> - 8.5.1-1
- Updated to release 8.5.1.

* Sun Oct 11 2009 Dag Wieers <dag@wieers.com> - 8.5.0-1
- Updated to release 8.5.0.

* Sun Mar 15 2009 Dag Wieers <dag@wieers.com> - 8.4.1-1
- Updated to release 8.4.1.

* Mon Mar 02 2009 Dag Wieers <dag@wieers.com> - 8.3.5-1
- Updated to release 8.3.5.

* Fri Jan 02 2009 Dag Wieers <dag@wieers.com> - 8.3.3-1
- Updated to release 8.3.3.

* Sun Dec 21 2008 Dag Wieers <dag@wieers.com> - 8.3.1-1
- Updated to release 8.3.1.

* Sun May 04 2008 Dag Wieers <dag@wieers.com> - 8.2.6-1
- Updated to release 8.2.6.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 8.2.5-1
- Updated to release 8.2.5.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 8.2.4-2
- Fixed  SyntaxError: future feature with_statement is not defined.

* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 8.2.4-1
- Updated to release 8.2.4

* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 8.2.3-1
- Updated to release 8.2.3.

* Wed Jul 25 2007 Dag Wieers <dag@wieers.com> - 8.2.2-1
- Updated to release 8.2.2.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 8.2.1-1
- Updated to release 8.2.1.

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
