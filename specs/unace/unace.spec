# $Id$
# Authority: dag

Summary: Linux program for uncompressing *.ace archives
Name: unace
Version: 2.50
Release: 1%{?dist}
License: Freeware
Group: Applications/Archiving
URL: http://www.winace.com/

Source: http://www.winace.com/files/linunace25.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386

%description
A compression tool that crunches the last free bit from your data, but takes
twice to ten times longer for compressing and - even worse - for extracting
your data probably will not work for you - or your customers.

On the other hand, a compression tool that deflates your files as quick as
lightning but leaves a lot of "air" in the compressed file will not take you
far either.

%prep
%setup -c

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -p -m0755 unace %{buildroot}%{_bindir}/unace
%{__chmod} -x licence

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc licence
%{_bindir}/unace

%changelog
* Mon Jan  9 2006 Matthias Saou <http://freshrpms.net/> 2.50-1
- Update to 2.50 ("22" -> "25").
- Change license tag from Shareware to Freeware.
- Include licence file, and remove its executable bit.
- Remove x86_64 from the exclusive arch, since this binary is i386 only.

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 2.20-0
- Initial package. (using DAR)

