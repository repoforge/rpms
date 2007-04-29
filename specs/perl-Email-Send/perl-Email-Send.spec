# $Id$
# Authority: dries
# Upstream: Ricardo Signes <rjbs$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Send

Summary: Send email
Name: perl-Email-Send
Version: 2.185
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Send/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Email-Send-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl module for sending mail.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Email::Send*
%{perl_vendorlib}/Email/Send.pm
%{perl_vendorlib}/Email/Send/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.185-1
- Updated to release 2.185.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 2.183-1
- Initial package.
