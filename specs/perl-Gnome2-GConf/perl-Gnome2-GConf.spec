# $Id$
# Authority: dag
# Upstream: Torsten Schönfeld <kaffeetisch$gmx,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gnome2-GConf

Summary: Perl wrapper for the GConf configuration engine
Name: perl-Gnome2-GConf
Version: 1.044
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gnome2-GConf/

Source: http://www.cpan.org/modules/by-module/Gnome2/Gnome2-GConf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Glib::CodeGen)
BuildRequires: pkgconfig
Requires: perl

%description
Gnome2-GConf is a Perl wrapper for the GConf configuration engine.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml NEWS README copyright.pod examples/
%doc %{_mandir}/man3/Gnome2::GConf.3pm*
%doc %{_mandir}/man3/Gnome2::GConf::*.3pm*
%dir %{perl_vendorarch}/Gnome2/
%{perl_vendorarch}/Gnome2/GConf/
%{perl_vendorarch}/Gnome2/GConf.pm
%dir %{perl_vendorarch}/auto/Gnome2/
%{perl_vendorarch}/auto/Gnome2/GConf/

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.044-1
- Updated to release 1.044.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.043-1
- Initial package. (using DAR)
