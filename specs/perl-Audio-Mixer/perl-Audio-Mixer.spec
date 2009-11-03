# $Id$
# Authority: dries
# Upstream: Sergey Gribov <sergey$sergey,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Audio-Mixer

Summary: Extension for Sound Mixer control
Name: perl-Audio-Mixer
Version: 0.7
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Audio-Mixer/

Source: http://www.cpan.org/modules/by-module/Audio/Audio-Mixer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Library to query / set various sound mixer parameters.

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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Audio/
%{perl_vendorarch}/Audio/Mixer.pm
%{perl_vendorarch}/Audio/volume.pl
%dir %{perl_vendorarch}/auto/Audio/
%{perl_vendorarch}/auto/Audio/Mixer/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Initial package.
