# $Id$
# Authority: dries
# Upstream: Nick Peskett <npeskett$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Audio-Wav

Summary: Module for reading Microsoft WAV files
Name: perl-Audio-Wav
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Audio-Wav/

Source: http://www.cpan.org/modules/by-module/Audio/Audio-Wav-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
These modules provide a method of reading & writing uncompressed
Microsoft WAV files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Audio/Wav.pm
%{perl_vendorlib}/Audio/Wav

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Updated to release 0.05.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
