Name: hunspell-ro
Summary: Romanian hunspell dictionaries
Version: 3.3
Release: 1%{?dist}
Source: http://downloads.sourceforge.net/rospell/%{name}.%{version}.tar.gz
Group: Applications/Text
URL: http://rospell.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Romanian hunspell dictionaries.

%prep
%setup -q -n %{name}.%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ro_RO.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING.GPL COPYING.LGPL COPYING.MPL
%{_datadir}/myspell/*

%changelog
* Mon Dec 07 2009 Caolan McNamara <caolanm@redhat.com> - 3.3-1
- Resolves: rhbz#544647 latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Sep 20 2006 Caolan McNamara <caolanm@redhat.com> - 3.2-1
- initial version
