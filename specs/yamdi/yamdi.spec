# $Id$
# Authority: dag

Summary: Yet Another MetaData Injector for FLV
Name: yamdi
Version: 1.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://yamdi.sourceforge.net/

Source: http://dl.sf.net/yamdi/yamdi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 
#Requires:

%description
yamdi is a metadata injector for FLV files. It adds the onMetaData event to
your FLV files.

%prep
%setup

%build
${CC:-%{__cc}} %{optflags} -fpic -o yamdi yamdi.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 yamdi %{buildroot}%{_bindir}/yamdi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README
%{_bindir}/yamdi

%changelog
* Sat Jan 05 2008 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
