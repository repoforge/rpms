# $Id$
# Authority: dries
# Upstream: S&#233;bastien Aperghis-Tramoni <maddingue$free,fr>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-Syslog-Mail

Summary: Parse mailer logs from syslog
Name: perl-Parse-Syslog-Mail
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-Syslog-Mail/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SAPER/Parse-Syslog-Mail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Parse mailer logs from syslog.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Parse::Syslog::Mail*
%{perl_vendorlib}/Parse/Syslog/Mail.pm
%dir %{perl_vendorlib}/Parse/Syslog/

%changelog
* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Updated to release 0.11.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
