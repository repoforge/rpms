# $Id$

# Authority: dries
# Upstream: Milivoj Ivkovic <>


%define real_name Mail-Sendmail
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Simple platform independent mailer
Name: perl-Mail-Sendmail
Version: 0.79
Release: 1
License: Unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Dispatch/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIVKOVIC/Mail-Sendmail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Simple platform independent e-mail from your perl script. Only requires
Perl 5 and a network connection.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Mail/Sendmail.pm

%changelog
* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.79-1
- Initial package.
