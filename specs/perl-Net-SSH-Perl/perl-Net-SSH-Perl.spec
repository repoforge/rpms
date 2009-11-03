# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SSH-Perl

Summary: Perl client interface to SSH
Name: perl-Net-SSH-Perl
Version: 1.34
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SSH-Perl/

Source: http://www.cpan.org/modules/by-module/Net/Net-SSH-Perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
#, perl-Math-Pari

%description
Net::SSH::Perl contains implementations of
both the SSH1 and SSH2 protocols.

%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi -e "s|use Socket;|use IO::Socket;\nuse Socket;|g;" lib/Net/SSH/Perl.pm

%build
echo "3" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/SSH/
%{perl_vendorlib}/Net/SSH/Perl.pm
%{perl_vendorlib}/Net/SSH/Perl/

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.34-1
- Updated to version 1.34.

* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 1.30-2
- Fix for error about missing object method 'blocking', thanks to Igor Bujna.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.30-1
- Updated to release 1.30.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.29-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.29-1
- Updated to release 1.29.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.28-1
- Updated to release 1.28.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.27-1
- Updated to release 1.27.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Initial package.
