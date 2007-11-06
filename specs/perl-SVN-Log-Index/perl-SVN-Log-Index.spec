# $Id$
# Authority: dries
# Upstream: Garrett Rooney <rooneg$electricjellyfish,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Log-Index

Summary: Index and search over Subversion commit logs
Name: perl-SVN-Log-Index
Version: 0.41
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Log-Index/

Source: http://search.cpan.org/CPAN/authors/id/N/NI/NIKC/SVN-Log-Index-%{version}.tar.gz
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
%doc CHANGES README TODO
%doc %{_mandir}/man3/*
%{_bindir}/*
%dir %{perl_vendorlib}/SVN/
%dir %{perl_vendorlib}/SVN/Log/
%{perl_vendorlib}/SVN/Log/Index.pm

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.41-1
- Updated to release 0.41.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Initial package.
