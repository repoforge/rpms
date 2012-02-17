# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define desktop_vendor rpmforge

Summary: Graphical tool for producing a multipage PDF from a scan
Name: gscan2pdf
Version: 1.0.1
Release: 1%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://gscan2pdf.sourceforge.net/

Source: http://dl.sf.net/project/gscan2pdf/gscan2pdf/%{version}/gscan2pdf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Goo::Canvas)
BuildRequires: perl(Gtk2::ImageView)
BuildRequires: perl(Sane) >= 0.02
Requires: djvulibre
Requires: gocr
Requires: goocanvas
Requires: perl(Cairo)
Requires: perl(Gtk2::Ex::PodViewer)
Requires: perl(PDF::API2)
Requires: perl(Sane) >= 0.02
Requires: perl(Set::IntSpan)
Requires: sane-backends >= 1.0.17
Requires: sane-frontends
Requires: unpaper
Requires: xdg-utils

%description
A GUI to ease the process of producing a multipage PDF from a scan.

%prep
%setup

### The Makefile from upstream has date in the future
touch -d "now" Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install locale_install icon_install
%find_lang %{name}

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

desktop-file-install --delete-original \
    --vendor="%{desktop_vendor}" \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/gscan2pdf.desktop

%post
update-desktop-database &>/dev/null ||:
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
update-desktop-database &>/dev/null ||:
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc History LICENCE
%doc %{_mandir}/man1/gscan2pdf.1*
%doc %{_mandir}/man1/scanadf-perl.1p.gz
%doc %{_mandir}/man1/scanimage-perl.1p.gz
%{_bindir}/gscan2pdf
%{_bindir}/scanadf-perl
%{_bindir}/scanimage-perl
%{_datadir}/applications/%{desktop_vendor}-gscan2pdf.desktop
%{_datadir}/gscan2pdf/
%{perl_vendorlib}/Gscan2pdf/
%{perl_vendorlib}/Gscan2pdf.pm
%{_datadir}/pixmaps/gscan2pdf.svg

%changelog
* Tue Feb 07 2012 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Thu Nov 03 2011 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Mon Feb 14 2011 Dag Wieers <dag@wieers.com> - 0.9.32-1
- Updated to release 0.9.32.

* Thu Jul 22 2010 Dag Wieers <dag@wieers.com> - 0.9.31-1
- Updated to release 0.9.31.

* Thu Jun 03 2010 Dag Wieers <dag@wieers.com> - 0.9.30-1
- Updated to release 0.9.30.

* Sun May 10 2009 Dag Wieers <dag@wieers.com> - 0.9.29-2
- Added missing perl(Cairo) dependency.

* Wed May 06 2009 Dag Wieers <dag@wieers.com> - 0.9.29-1
- Updated to release 0.9.29.

* Fri May 01 2009 Dag Wieers <dag@wieers.com> - 0.9.28-1
- Updated to release 0.9.28.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.9.27-1
- Updated to release 0.9.27.

* Tue Dec 09 2008 Dag Wieers <dag@wieers.com> - 0.9.26-1
- Initial package. (using DAR)
