# $Id$

# Authority: dries
# Upstream: Garrett Rooney <rooneg$electricjellyfish,net>

%define real_name SVN-Log-Index
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Index and search over Subversion commit logs
Name: perl-SVN-Log-Index
Version: 0.30
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Log-Index/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROONEG/SVN-Log-Index-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, subversion-perl, perl-Module-Build

%description
SVN::Log::Index builds a Plucene index of commit logs from any number of
Subversion repositories and allows you to do arbitrary full text
searches over them.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES TODO
%doc %{_mandir}/man3/*
%{perl_vendorlib}/SVN/Log/Index.pm
%{_bindir}/*

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Initial package.
