# $Id$
# Authority: shuff
# Upstream: Lee Eakin <leakin$dfw,nostrum,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Rsync

Summary: perl module interface to rsync(1)
Name: perl-%{real_name}
Version: 0.43
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Rsync/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LEAKIN/File-Rsync-%{version}.tar.gz
Patch0: %{name}_rsync-pathfind.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 5.004
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util)
BuildRequires: rsync >= 2.3.2
Requires: perl >= 5.004
Requires: rsync >= 2.3.2

%description
Perl Convenience wrapper for the rsync(1) program. Written for rsync-2.3.2 and
updated for rsync-2.6.0 but should perform properly with most recent versions.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog MANIFEST README TODO
%doc %{_mandir}/man?/*
%dir %{perl_vendorarch}/File/
%{perl_vendorarch}/File/Rsync.pm
%{perl_vendorarch}/File/Rsync/*.pm

%changelog
* Wed Oct 28 2009 Steve Huff <shuff@vecna.org> - 0.43-1
- Updated to version 0.43.

* Fri Oct 02 2009 Steve Huff <shuff@vecna.org> - 0.42-1
- Initial package.
