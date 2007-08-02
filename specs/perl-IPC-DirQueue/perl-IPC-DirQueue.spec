# $Id$
# Authority: dries
# Upstream: Justin Mason <jmason$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-DirQueue

Summary: Disk-based many-to-many task queue
Name: perl-IPC-DirQueue
Version: 0.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-DirQueue/

Source: http://search.cpan.org//CPAN/authors/id/J/JM/JMASON/IPC-DirQueue-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Disk-based many-to-many task queue.

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
%doc BUGS CHANGES README.dist TODO
%doc %{_mandir}/man3/IPC::DirQueue*
%doc %{_mandir}/man1/dq-*
%{perl_vendorlib}/IPC/DirQueue.pm
%{perl_vendorlib}/IPC/DirQueue/
%{_bindir}/dq-deque
%{_bindir}/dq-indexd
%{_bindir}/dq-list
%{_bindir}/dq-server
%{_bindir}/dq-submit

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
