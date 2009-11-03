# $Id$
# Authority: dag
# Upstream: Emmanuele Bassi <emmanuele$emmanuelebassi,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gnome2-Print

Summary: Perl wrapper for the Gnome Print utilities
Name: perl-Gnome2-Print
Version: 1.000
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gnome2-Print/

Source: http://www.cpan.org/modules/by-module/Gnome2/Gnome2-Print-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: libgnomeprintui22-devel >= 2.2
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Gtk2::CodeGen)
BuildRequires: perl(Cairo::Install::Files)
Requires: perl

%description
Gnome2-Print is a Perl wrapper for the Gnome Print utilities.

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
%doc AUTHORS ChangeLog MANIFEST META.yml NEWS README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Gnome2/
%{perl_vendorarch}/Gnome2/Print.pm
%{perl_vendorarch}/Gnome2/Print/
%dir %{perl_vendorarch}/auto/Gnome2/
%{perl_vendorarch}/auto/Gnome2/Print/

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.000-1
- Initial package. (using DAR)
