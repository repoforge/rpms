# $Id$

# Authority: dries
# Upstream:

%define real_name Mail-Sendmail

Summary: Simple platform independent mailer
Name: perl-Mail-Sendmail
Version: 0.79
Release: 1
License: Unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Dispatch/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIVKOVIC/Mail-Sendmail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Simple platform independent e-mail from your perl script. Only requires
Perl 5 and a network connection.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Mail/Sendmail/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{_libdir}/perl5/vendor_perl/*/Mail/Sendmail.pm

%changelog
* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.79-1
- Initial package.
