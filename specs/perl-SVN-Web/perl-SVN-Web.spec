# $Id$

# Authority: dries
# Upstream: clkao$clkao,org

%define real_name SVN-Web
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Subversion repository web frontend
Name: perl-SVN-Web
Version: 0.38
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Web/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/SVN-Web-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# BuildRequires: perl, perl-Template, perl-YAML, perl-XML-RSS, perl-Text-Diff
# BuildRequires: perl-Locale-Maketext-Simple, subversion-perl

%description
SVN::Web is a subversion repository web frontend.

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/SVN/Web.pm
%{perl_vendorlib}/SVN/Web/*

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Updated to release 0.38.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Initial package.
