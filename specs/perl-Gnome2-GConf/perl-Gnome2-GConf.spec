# $Id$
# Authority: dag
# Upstream: Emmanuele Bassi <emmanuele$emmanuelebassi,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gnome2-GConf

Summary: Perl wrapper for the GConf configuration engine
Name: perl-Gnome2-GConf
Version: 1.043
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gnome2-GConf/

Source: http://www.cpan.org/modules/by-module/Gnome2/Gnome2-GConf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker), perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
BuildRequires: perl(Glib::CodeGen)
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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml NEWS README
%doc %{_mandir}/man3/Gnome2::GConf.3pm*
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Gnome2/
%{perl_vendorarch}/Gnome2/GConf.pm
%{perl_vendorarch}/Gnome2/GConf/
%dir %{perl_vendorarch}/auto/Gnome2/
%{perl_vendorarch}/auto/Gnome2/GConf/

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.043-1
- Initial package. (using DAR)
