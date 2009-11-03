# $Id$
# Authority: dag
# Upstream: Jan Akkerman <jan$it,uu,se>
# Upstream: <html2ps-users-request$list,it,uu,se>

Summary: HTML to PostScript converter
Name: html2ps
%define real_version 1.0b5
Version: 1.0
Release: 0.b5.2%{?dist}
License: GPL
Group: Applications/File
URL: http://user.it.uu.se/~jan/html2ps.html

Source: http://user.it.uu.se/~jan/html2ps-%{real_version}.tar.gz
Patch0: html2ps-1.0b5-conf.patch
Patch1: html2ps-1.0b5-perl_path.patch
Patch2: html2ps-1.0b5-open.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
The Perl script html2ps converts HTML to PostScript. It would have
more capabilities if you have some of these packages installed:
ImageMagick, netpbm-progs, libjpeg-progs, perl-libwww, ghostscript,
tetex, tetex-dvips - see documentation for details.

html2ps can be used as ImageMagick delegate to convert from HTML.

%package -n xhtml2ps
Summary: GUI frontend for html2ps, a HTML-to-PostScript converter
Group: Applications/File
Requires: %{name} = %{version}-%{release}
Requires: tk

%description -n xhtml2ps
xhtml2ps is freely-available GUI frontend for html2ps, a
HTML-to-PostScript converter.


%prep
%setup -n %{name}-%{real_version}
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%{__perl} -pi.orig -e '
        s|\@CONFDIR\@|%{_sysconfdir}|;
        s|\@DOCDIR\@|%{_docdir}/%{name}-%{version}|;
    ' html2ps html2ps.1

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 html2ps %{buildroot}%{_bindir}/html2ps
%{__install} -Dp -m0755 contrib/xhtml2ps/xhtml2ps %{buildroot}%{_bindir}/xhtml2ps
%{__install} -Dp -m0644 html2psrc %{buildroot}%{_sysconfdir}/html2psrc
%{__install} -Dp -m0644 html2ps.1 %{buildroot}%{_mandir}/man1/html2ps.1
%{__install} -Dp -m0644 html2psrc.5 %{buildroot}%{_mandir}/man5/html2psrc.5

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING html2ps.html README sample
%doc %{_mandir}/man1/html2ps.1*
%doc %{_mandir}/man5/html2psrc.5*
%config(noreplace) %{_sysconfdir}/html2psrc
%{_bindir}/html2ps

%files -n xhtml2ps
%defattr(-, root, root, 0755)
%doc contrib/xhtml2ps/LICENSE contrib/xhtml2ps/README
%{_bindir}/xhtml2ps

%changelog
* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 1.0-0.b5.2
- Fix group tag.

* Tue Oct 30 2007 Dag Wieers <dag@wieers.com> - 1.0-0.b5.1
- Fixed a typo in the Requires of xhtml2ps. (Dave Shield)

* Tue Sep 25 2007 Dag Wieers <dag@wieers.com> - 1.0-0.b5
- Initial package. (using DAR)
