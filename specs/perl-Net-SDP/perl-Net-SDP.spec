# $Id$
# Authority: dries
# Upstream: Nicholas J Humfrey <njh$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SDP

Summary: Session Description Protocol (rfc2327)
Name: perl-Net-SDP
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SDP/

Source: http://search.cpan.org//CPAN/authors/id/N/NJ/NJH/Net-SDP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Module::Build)

%description
Session Description Protocl (rfc2327)

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Net::SDP*
%doc %{_mandir}/man1/sdp2rat*
%{perl_vendorlib}/Net/SDP.pm
%{perl_vendorlib}/Net/SDP/
%{_bindir}/sdp2rat

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
