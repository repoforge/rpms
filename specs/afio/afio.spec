# $Id$
# Authority: dag

Summary: Archiver program which writer CPIO-format archives
Name: afio
Version: 2.5
Release: 2%{?dist}
License: LGPL
Group: Applications/Archiving
URL: http://www.ibiblio.org/pub/Linux/system/backup/

Source: http://www.ibiblio.org/pub/Linux/system/backup/afio-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
afio makes cpio-format archives. It deals somewhat gracefully with input
data corruption, supports multi-volume archives during interactive
operation, and can make compressed archives that are much safer than
compressed tar or cpio archives. Afio is best used as an `archive engine'
in a backup script.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 afio %{buildroot}%{_bindir}/afio
%{__install} -Dp -m0444 afio.1 %{buildroot}%{_mandir}/man1/afio.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY INSTALLATION PORTING README SCRIPTS afio.lsm script1 script2 script3 script4
%doc %{_mandir}/man1/afio.1*
%{_bindir}/afio

%changelog
* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 2.5-2
- Fix group tag.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
