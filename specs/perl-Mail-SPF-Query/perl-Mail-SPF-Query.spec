# $Id$
# Authority: dries
# Upstream: Julian Mehnle <julian$mehnle,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-SPF-Query

Summary: Query a Sender Policy Framework
Name: perl-Mail-SPF-Query
Version: 1.999.1
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-SPF-Query/

Source: http://search.cpan.org/CPAN/authors/id/J/JM/JMEHNLE/mail-spf-query/Mail-SPF-Query-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
With this module, you can use a Sender Policy Framework.

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
%doc CHANGES README
%doc %{_mandir}/man3/Mail::SPF::Query*
%doc %{_mandir}/man1/spf*
%{_bindir}/spfd
%{_bindir}/spfquery
%{perl_vendorlib}/Mail/SPF/Query.pm

%changelog
* Fri Mar  3 2006 Dries Verachtert <dries@ulyssis.org> - 1.999.1-1
- Initial package.
