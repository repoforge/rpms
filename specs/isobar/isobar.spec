# $Id$
# Authority: dag
# Upstream: newhren <colimit@gmail.com>

Summary: Tool to extract a boot image from an ISO file
Name: isobar
Version: 1.03
Release: 1
License: GPL
Group: Applications/File
URL: http://colimit.googlepages.com/

Source: http://colimit.googlepages.com/isobar.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
isobar is a tool to extract a boot image from an ISO file. It was based
on a free open-source DOS utility with the same name from the shsucd
package.

%prep
%setup -cT
%{__cp} -v %{SOURCE0} isobar.c

%build
%{__cc} %{optflags} -o isobar isobar.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 isobar %{buildroot}%{_bindir}/isobar

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/isobar

%changelog
* Thu May 21 2009 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
