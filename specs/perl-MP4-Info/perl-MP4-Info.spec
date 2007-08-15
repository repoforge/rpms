# $Id$
# Authority: dries
# Upstream: Jonathan Harris <jhar$spamcop,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name MP4-Info

Summary: Fetch info from MPEG-4 files
Name: perl-MP4-Info
Version: 1.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MP4-Info/

Source: http://search.cpan.org//CPAN/authors/id/J/JH/JHAR/MP4-Info-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Fetch info from MPEG-4 files (.mp4, .m4a, .m4p, .3gp).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/MP4::Info*
%{perl_vendorlib}/MP4/Info.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Initial package.
