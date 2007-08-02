# $Id$
# Authority: dries
# Upstream: Ricardo Signes <rjbs$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME-Creator

Summary: Constructor for Email::MIME
Name: perl-Email-MIME-Creator
Version: 1.453
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME-Creator/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Email-MIME-Creator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This package contains a constructor for Email::MIME.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Email::MIME::Creator*
%{perl_vendorlib}/Email/MIME/Creator.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.453-1
- Updated to release 1.453.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.451
- Initial package.
