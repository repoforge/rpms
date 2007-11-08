# $Id$
# Authority: dries
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Compress-Bzip2

Summary: Handle bzip2 compressed files
Name: perl-IO-Compress-Bzip2
Version: 2.003
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Compress-Bzip2/

Source: http://search.cpan.org//CPAN/authors/id/P/PM/PMQS/IO-Compress-Bzip2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A module for handling bzip2 compressed files.

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
%doc %{_mandir}/man3/IO::Compress::Bzip2*
%doc %{_mandir}/man3/IO::Uncompress::Bunzip2*
%{perl_vendorlib}/IO/Compress/Bzip2.pm
%{perl_vendorlib}/IO/Compress/Adapter/
%{perl_vendorlib}/IO/Uncompress/Bunzip2.pm
%{perl_vendorlib}/IO/Uncompress/Adapter/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.003-1
- Initial package.
