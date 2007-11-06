# $Id$
# Authority: dries
# Upstream: Scott Gifford <sgifford$suspectclass,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-FTP-RetrHandle

Summary: Tied or IO::Handle-compatible interface to a file retrieved by FTP
Name: perl-Net-FTP-RetrHandle
Version: 0.2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-FTP-RetrHandle/

Source: http://search.cpan.org//CPAN/authors/id/G/GI/GIFF/Net-FTP-RetrHandle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Tied or IO::Handle-compatible interface to a file retrieved by FTP.

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
%doc NEWS TODO
%doc %{_mandir}/man3/Net::FTP::RetrHandle*
%{perl_vendorlib}/Net/FTP/RetrHandle.pm
%dir %{perl_vendorlib}/Net/FTP/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
