# $Id$
# Authority: dag

%define real_version 02l

Summary: MPEG Audio Layer II VBR encoder
Name: toolame
Version: 0.0.%{real_version}
Release: 1%{?dist}
License: LGPL
Group: Applications/Multimedia
URL: http://toolame.sourceforge.net/

Source: http://dl.sf.net/sourceforge/toolame/toolame-%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
PEG Audio Layer II VBR encoder

%prep
%setup -n %{name}-%{real_version}

%build
%ifarch x86_64
#%{__make} ARCH="-m64 -mtune=generic"
%{__make} ARCH="-m64"
%else
%{__make}
%endif

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 toolame %{buildroot}%{_bindir}/toolame

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc FUTURE HISTORY LGPL.txt README html/
%{_bindir}/toolame

%changelog
* Thu Mar 29 2007 Dag Wieers <dag@wieers.com> - 0.0.02l-1
- Initial package. (using DAR)
