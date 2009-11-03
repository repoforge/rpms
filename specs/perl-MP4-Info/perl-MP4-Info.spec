# $Id$
# Authority: dries
# Upstream: Jonathan Harris <jhar$spamcop,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MP4-Info

Summary: Fetch info from MPEG-4 files
Name: perl-MP4-Info
Version: 1.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MP4-Info/

Source: http://www.cpan.org/modules/by-module/MP4/MP4-Info-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Fetch info from MPEG-4 files (.mp4, .m4a, .m4p, .3gp).

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
%doc INSTALL Info.pm MANIFEST META.yml README
%doc %{_mandir}/man3/MP4::Info.3pm*
%dir %{perl_vendorlib}/MP4/
#%{perl_vendorlib}/MP4/Info/
%{perl_vendorlib}/MP4/Info.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Initial package.
