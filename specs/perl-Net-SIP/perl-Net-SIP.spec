# $Id$
# Authority: dries
# Upstream: Steffen Ullrich <Steffen_Ullrich$genua,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SIP

Summary: Framework for SIP and Voice Over IP
Name: perl-Net-SIP
Version: 0.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SIP/

Source: http://search.cpan.org//CPAN/authors/id/S/SU/SULLR/Net-SIP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Framework SIP (Voice Over IP, RFC3261).

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
%doc %{_mandir}/man3/Net::SIP*
%{perl_vendorlib}/Net/SIP.p*
%{perl_vendorlib}/Net/SIP/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Initial package.
