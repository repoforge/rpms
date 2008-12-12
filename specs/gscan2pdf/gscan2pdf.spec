# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define desktop_vendor rpmforge

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

Summary: Graphical tool for producing a multipage PDF from a scan
Name: gscan2pdf
Version: 0.9.27
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://gscan2pdf.sourceforge.net/

Source: http://dl.sf.net/gscan2pdf/gscan2pdf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Gtk2::ImageView)
BuildRequires: perl(Sane) >= 0.02
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: djvulibre
Requires: gocr
Requires: perl(Gtk2::Ex::PodViewer)
Requires: perl(PDF::API2)
Requires: perl(Sane) >= 0.02
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

%if %{!?_without_freedesktop:1}0
desktop-file-install --delete-original \
    --vendor="%{desktop_vendor}" \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/gscan2pdf.desktop
%endif

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
%doc %{_mandir}/man1/scanadf.pl.1p*
%doc %{_mandir}/man1/scanimage.pl.1p*
%{_bindir}/gscan2pdf
%{_bindir}/scanadf.pl
%{_bindir}/scanimage.pl
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-gscan2pdf.desktop}
%{?_without_freedesktop:%{_datadir}/applications/gscan2pdf.desktop}
%{_datadir}/gscan2pdf/
%{perl_vendorlib}/Gscan2pdf.pm

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.9.27-1
- Updated to release 0.9.27.

* Tue Dec 09 2008 Dag Wieers <dag@wieers.com> - 0.9.26-1
- Initial package. (using DAR)
