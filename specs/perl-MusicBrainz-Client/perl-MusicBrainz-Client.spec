# $Id$
# Authority: dag
# Upstream: Sander van Zoest <svanzoest$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MusicBrainz-Client

Summary: Perl module that implements the MusicBrainz Client API
Name: perl-MusicBrainz-Client
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MusicBrainz-Client/

Source: http://www.cpan.org/modules/by-module/MusicBrainz/MusicBrainz-Client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-MusicBrainz-Client is a Perl module that implements the
MusicBrainz Client API.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/MusicBrainz/
%{perl_vendorarch}/MusicBrainz/Client/
%{perl_vendorarch}/MusicBrainz/Client.pm
%{perl_vendorarch}/MusicBrainz/simple_demo.pl
%dir %{perl_vendorarch}/auto/MusicBrainz/
%{perl_vendorarch}/auto/MusicBrainz/Client/

%changelog
* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
