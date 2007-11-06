# $Id$
# Authority: dries
# Upstream: John Peacock <jpeacock$rowman,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Notify-Mirror

Summary: Keep a mirrored working copy of a repository path
Name: perl-SVN-Notify-Mirror
Version: 0.036
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Notify-Mirror/

Source: http://search.cpan.org//CPAN/authors/id/J/JP/JPEACOCK/SVN-Notify-Mirror-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker), perl(Module::Build)

%description
Keep a mirrored working copy of a repository path.

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
%doc Changes README
%doc %{_mandir}/man3/SVN::Notify::Mirror*
%{perl_vendorlib}/SVN/Notify/Mirror.pm
%{perl_vendorlib}/SVN/Notify/Mirror/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.036-1
- Initial package.
