# $Id$
# Authority: dag
# Upstream: Salvador Fandino <sfandino$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-OpenSSH

Summary: Perl module named Net-OpenSSH
Name: perl-Net-OpenSSH
Version: 0.52
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-OpenSSH/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SALVA/Net-OpenSSH-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge
Requires: openssh-clients >= 4.1
Requires: perl

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

%filter_setup

%description
Perl SSH client package implemented on top of OpenSSH.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

# fix permissions on sample scripts
%{__chmod} +x sample/*.pl

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README sample/
%doc %{_mandir}/man3/Net::OpenSSH.3pm*
%doc %{_mandir}/man3/Net::OpenSSH::*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/OpenSSH/
%{perl_vendorlib}/Net/OpenSSH.pm

%changelog
* Thu Aug 22 2011 Giacomo Tenaglia <Giacomo.Tenaglia@cern.ch> - 0.52-1
- Upgrade to version 0.52.
- Updated description.

* Tue Jun 22 2010 Dag Wieers <dag@wieers.com> - 0.36-1
- Initial package. (using DAR)
