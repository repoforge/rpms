# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SSH-Perl

Summary: Perl client interface to SSH
Name: perl-Net-SSH-Perl
Version: 1.27
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SSH-Perl/

Source: http://www.cpan.org/modules/by-module/Net/Net-SSH-Perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-Math-Pari

%description
Net::SSH::Perl contains implementations of
both the SSH1 and SSH2 protocols.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
#%{perl_vendorlib}/NAMEDIR.pm
#%{perl_vendorlib}/NAMEDIR/*

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.27-1
- Updated to release 1.27.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Initial package.
